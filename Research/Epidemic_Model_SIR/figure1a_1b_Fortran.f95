PROGRAM random_walk2D

    !======================================================================================================!
    ! DECLARAÇÃO DE VARIÁVEIS                                                                              !
    !======================================================================================================!

    IMPLICIT NONE

    !Variaveis para mostrar o instante de inicio e termino
    INTEGER :: inicio,termino,cputime,cpuhour,cpumin,cpusec  ! IMPRIME A DATA E HORA
    INTEGER :: valuei(8),valuef(8)                           ! OBTEM A DATA E HORA DE INICIO E FIM
    CHARACTER(LEN=30) :: date,time,zone   ! USADO PARA ENCONTRAR A DATA E HORARIO DE INICIO E TERMINO
    

    INTEGER :: t0, t1, t2, t3
    INTEGER :: i1, i2, i3, i4, i5, i6, i7, i8 
    INTEGER :: j1, j2, j3, j4, j5, j6, j7, j8, j9 !indices dos for
    !64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768

!Se Nv > 32000, coloque Nmax = 300, caso contrario use Nmax = 200
    INTEGER, PARAMETER :: Q = 50, Nv = 256, samples = 1, Nmax = 200   !Nv tem de ser par 
    INTEGER :: seed, estado(Nv,Q), Nneig(Nv), neighbors(Nv,Nmax), ind0, viz
    REAL, PARAMETER ::  v = 1.0, p_walk = 0.5, pi = 3.14159265 !p_walk = w
    REAL :: L, pos_x(Nv,Q+1), pos_y(Nv,Q+1), dist2, p_in = 0.9, rho, delxy, d_int
    REAL :: ran2, theta, newx, newy, new_x_p, new_y_p, prob_infectar, cont_sus(Q), cont_inf(Q), cont_rec(Q)
    INTEGER :: N_viz_inf, Nv_sqrt


!v = distancia percorrida quando move
! estado = objeto que guarda a informacao do estado de cada individuo ao longo do tempo
!estado(i,t) = estado do individuo i no tempo t
! estado = 0 implica individuo suceptivel
! estado = 1 implica individuo infectado
! estado = 2 implica individuo recuperado

!Nneig(i) = numero de vizinhos do individuo i, essa variavel sera zerada no inicio de cada iteracao
!neighbors(i1,i2) identifica quem sao os vizinhos de i1
!neighbors(i1,1) = primeiro vizinho de i1
!neighbors(i1,2) = segundo vizinho de i1
!neighbors(i1,3) = terceiro vizinho de i1
!!neighbors(i1,i2) = 0 implica que nao ha vizinho
!essa sequencia nao tem a ver com quem esta mais perto ou mais longe

    
    !======================================================================================================!
    !Abrindo os arquivos a serem usados.
    !OPEN(10,FILE='eqb_dados-L_'//rede//'-samp_'//termal//'-step_'//pmc//'-'//semente//'.dat')
    open (unit=1,file='posicao_x.csv',action="write",status="replace")
    open (unit=2,file="posicao_y.csv",action="write",status="replace")
    open (unit=3,file="parametros.csv",action="write",status="replace")
    open (unit=5,file="interacoes.csv",action="write",status="replace")
    open (unit=7,file="estado.csv",action="write",status="replace")
    open (unit=10,file='informacoes.txt',action="write",status="replace")
    !======================================================================================================!  

    !======================================================================================================!
    ! IMPRIMINDO A DATA E HORARIO De inicio DA SIMULACAO BEM COMO O TEMPO TOTAL DE SIMULACAO              !

    CALL DATE_AND_TIME(date,time,zone,valuei)   ! SUBROUTINA INTRINSECA QUE IMPRIME DATA E HORA DE INICIO

    PRINT'("Data de inicio:",I2," / ",I2," / ",I4,". &
    &Horario de inicio:",I2," : ",I2," : ",I2)',valuei(3),valuei(2),valuei(1),valuei(5:7)
    inicio=valuei(5)*3600+valuei(6)*60+valuei(7)   ! OBTEM A HORA QUE A SIMULACAO COMECOU, EM SEGUNDOS

    WRITE(10,'("DATA DE INICIO  ==> ",I2," / ",I2," / ",I4,". &
    &HORARIO DE INICIO  ==> ",I2," : ",I2," : ",I2)') valuei(3),valuei(2),valuei(1),valuei(5:7)
    !======================================================================================================!

!!!!!!!!!!!!!!!!!!Condicoes Iniciais!!!!!!!!!!!!!!!!!!!!!!!!!!!!

rho = 512 / 1E4 !densidade considerando 256 individuos em um quadrado de lado 100
L = sqrt(Nv/rho)
write(10,*) "Densidade:", rho
write(10,*) "Lado do quadrado:", L

!Em Fortran, o primeiro indice de um vetor e 1
!A simulacao comeca no tempo t = 1
seed=1

cont_sus = 0; cont_inf = 0; cont_rec = 0

Nv_sqrt = INT(SQRT(1.0*Nv))
delxy = L / (1.0 * Nv_sqrt)
d_int = delxy + delxy/10.0 

DO i8 = 1,samples
    
    ! !definindo posicoes aleatorias
    ! DO i1 = 1, Nv 
    !   pos_x(i1,1) = L*ran2(seed)
    !   pos_y(i1,1) = L*ran2(seed)
    ! ENDDO

    !grid regular

    j9 = 1
    DO i1 = 1, Nv_sqrt
        DO i2 = 1, Nv_sqrt
            pos_x(j9,1) = delxy/2 +(i1-1) * delxy
            pos_y(j9,1) = delxy/2 +(i2-1) * delxy
            j9 = j9 + 1
        ENDDO
    ENDDO
     
    !estado = 0
    
    !Condicao inicial 1: populacao aleatoria
    ! DO j7 = 1, Nv 
    !   estado(j7,1) = INT(2.0*ran2(seed)) !aleatorio entre 0 e 1
    !   !print*,j7,1,estado(j7,1)
    ! ENDDO
    
    !Condicao inicial 2: apenas individuo um infectado
    ind0 = INT(Nv*ran2(seed))+1
    estado(:,1) = 0
    estado(ind0,1) = 1
    
    !!!!!!!!!!!!!!!!!!!!!!Evolucao temporal!!!!!!!!!!!!!!!!!!!!!!!!
    
    DO t1=1,Q !laco temporal
        IF (t1 .GT. 1) THEN !igualando o estado no tempo t1 com o estado em t1-1
            DO i7 = 1, Nv
                estado(i7,t1) = estado(i7,t1-1)
                !print*,i7, t1,estado(i7,t1)
            ENDDO
        ENDIF
        neighbors = 0; Nneig = 0
        !print*,"Iteracao:",t1
        DO i2 = 1, Nv
            CALL up_neig(i2,t1,Nv,Q,L,pos_x,pos_y,d_int,Nneig,neighbors,Nmax)
        ENDDO
        IF (t1 .LT. Q) THEN !so calcula as posicoes ate t1 = Q
            DO i3 = 1, Nv
                IF (Nneig(i3) .GT. 0) THEN
                    N_viz_inf = 0
                    IF ((t1 .GT. 1) .AND. (estado(i3,t1) .EQ. 0)) THEN !transmissao da infeccao
                        DO i2 = 1, Nneig(i3) !procurando vizinhos infectados
                            viz = neighbors(i3,i2)
                            IF (estado(viz,t1) .EQ. 1) N_viz_inf = N_viz_inf + 1
                        ENDDO 
                        prob_infectar = N_viz_inf*p_in/Nneig(i3)
                        IF ((N_viz_inf .GE. 1) .AND. (ran2(seed) .LT. prob_infectar)) estado(i3,t1) = 1
                    ENDIF
                    pos_x(i3,t1+1) = new_x_p(pos_x(i3,t1),v,L,p_walk,seed) 
                    pos_y(i3,t1+1) = new_y_p(pos_y(i3,t1),v,L,p_walk,seed)
                ELSE
                    pos_x(i3,t1+1) = newx(pos_x(i3,t1),v,seed,L)
                    pos_y(i3,t1+1) = newy(pos_y(i3,t1),v,seed,L)
                ENDIF
                IF ((estado(i3,t1) .EQ. 1) .AND. (ran2(seed) .GT. p_in)) estado(i3,t1) = 2
            ENDDO
        ENDIF
        DO j5=1,Nv
            IF ((samples .EQ. 1) .OR. (i8 .EQ. samples)) THEN
                IF (Nneig(j5) .GT. 0) THEN
                    write(5,*) t1,j5-1,Nneig(j5),(neighbors(j5,j6)-1, j6=1,Nneig(j5)) 
                ELSE
                    write(5,*) t1,j5-1,Nneig(j5)
                ENDIF
            ENDIF
            ! IF (estado(j5,t1) .EQ. 0) THEN 
            !     cont_sus(t1) = cont_sus(t1) + 1
            ! ELSE IF (estado(j5,t1) .EQ. 1) THEN
            !     cont_inf(t1) = cont_inf(t1) + 1 
            ! ELSE IF (estado(j5,t1) .EQ. 2) THEN
            !     cont_rec(t1) = cont_rec(t1) + 1
            ! ELSE
            !     print*,'Algo esta errado!',j5, t1,estado(j5,t1)
            ! ENDIF
        ENDDO
    ENDDO
ENDDO
    !!!!!!!!!!!!!!! fim do do das amostras!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    close(unit = 5)
    
    !!!!!!!!!!!!!!!!!!!Salvando dados nos arquivos!!!!!!!!!!!!!!!!!!!!!!!!!!!

    DO t2=1,Q
        write(1,*) (pos_x(i5,t2), i5 = 1,Nv)
        write(2,*) (pos_y(i4,t2), i4 = 1,Nv)
        write(7,*) (estado(j4,t2), j4 = 1,Nv)
    ENDDO

    close(unit = 1)
    close(unit = 2)
    close(unit = 7)
    close(unit = 8)
    
    write(3,*) Nv, Q, L, v, p_walk, d_int, p_in, samples

    close(unit = 3)
    
    write(10,*) "***************************"
    write(10,*) "Parametros iniciais:"
    write(10,*) "Numero de individuos Nv:", Nv
    write(10,*) "Numero de iteracoes no tempo Q:", Q
    write(10,*) "Probabilidade de andar durante interacao p_walk:", p_walk
    write(10,*) "Distancia deslocada em cada iteracao v:", v
    write(10,*) "Distancia maxima para ser vizinho d_int:",d_int
    write(10,*) "Probabilidade de infecao p_in:", p_in
    write(10,*) "Numero de amostras samples:", samples
    write(10,*) "Lado do quadrado L:", L
    
    
    !======================================================================================================!
    ! IMPRIMINDO A DATA E HORARIO DO TERMINO DA SIMULACAO BEM COMO O TEMPO TOTAL DE SIMULACAO              !
write(10,*) "**************************"

    CALL DATE_AND_TIME(date,time,zone,valuef)
    PRINT'("DATA DE TERMINO ==> ",I2," / ",I2," / ",I4,". &
    &HORARIO DE TERMINO ==> ",I2," : ",I2," : ",I2)',valuef(3),valuef(2),valuef(1),valuef(5:7)
    termino=valuef(5)*3600+valuef(6)*60+valuef(7)

    cputime=termino-inicio
    cpuhour=INT(cputime/3600)
    cpumin =INT((cputime-cpuhour*3600)/60) 
    cpusec =cputime-(cpuhour*3600+cpumin*60)

    PRINT'("TEMPO TOTAL DE SIMULACAO PARA A REDE:&
    & ",I4," HORAS, ",I2," MINUTOS E ",I2," SEGUNDOS",/)',cpuhour,cpumin,cpusec
    WRITE(10,'("DATA DE TERMINO ==> ",I2," / ",I2," / ",I4,". &
    &HORARIO DE TERMINO ==> ",I2," : ",I2," : ",I2)') valuef(3),valuef(2),valuef(1),valuef(5:7)
    WRITE(10,'("TEMPO TOTAL DE SIMULACAO PARA A REDE :&
    & ",I4," HORAS, ",I2," MINUTOS E ",I2," SEGUNDOS",/)') cpuhour,cpumin,cpusec

    !======================================================================================================!

    STOP

END PROGRAM random_walk2D

SUBROUTINE up_neig(i2,t1,Nv,Q,L,pos_x,pos_y,d_int,Nneig,neighbors,Nmax)
    IMPLICIT NONE
    INTEGER :: j2, i2, t1, Nv, Q, Nmax
    INTEGER :: Nneig(Nv), neighbors(Nv,Nmax)
    REAL :: L, d_int, pos_x(Nv,Q+1), pos_y(Nv,Q+1), d2_r
    !REAL :: x_vir, y_vir, L!, d2_x, d2_y, d2_xy
    DO j2 = i2, Nv 
        IF (i2 .NE. j2) THEN
            d2_r = (pos_x(i2,t1) - pos_x(j2,t1))**2.0 + (pos_y(i2,t1) - pos_y(j2,t1))**2.0
            !d2_x = (pos_x(i2,t1) - x_vir(j2,t1,L,Nv,Q,pos_x))**2.0 + (pos_y(i2,t1) - pos_y(j2,t1))**2.0
            !d2_y = (pos_x(i2,t1) - pos_x(j2,t1))**2.0 + (pos_y(i2,t1) - y_vir(j2,t1,L,Nv,Q,pos_y))**2.0
            !d2_xy = (pos_x(i2,t1) - x_vir(j2,t1,L,Nv,Q,pos_x))**2.0 + (pos_y(i2,t1) - y_vir(j2,t1,L,Nv,Q,pos_y))**2.0
            !IF ((d2_r .LE. d_int**2.0) .OR. (d2_x .LE. d_int**2.0) .OR. (d2_y .LE. d_int**2.0) .OR. (d2_xy .LE. d_int**2.0))  THEN
            IF (d2_r .LE. d_int**2.0)  THEN
                Nneig(i2) = Nneig(i2) +1; Nneig(j2) = Nneig(j2) +1; !incrementando o n. de vizinho
                neighbors(i2,Nneig(i2)) = j2; neighbors(j2,Nneig(j2)) = i2;
            ENDIF
        ENDIF
    ENDDO
END SUBROUTINE up_neig


REAL FUNCTION x_vir(j2,t1,L,Nv,Q,pos_x)
    IMPLICIT NONE
    INTEGER :: j2, t1, Nv, Q
    REAL :: pos_x(Nv,Q+1), L
    IF (pos_x(j2,t1) .GT. L/2) THEN
        x_vir = pos_x(j2,t1) - L
    ELSE
        x_vir = pos_x(j2,t1) + L
    ENDIF
    RETURN
END


REAL FUNCTION y_vir(j2,t1,L,Nv,Q,pos_y)
    IMPLICIT NONE
    INTEGER :: j2, t1, Nv, Q
    REAL :: pos_y(Nv,Q+1), L
    IF (pos_y(j2,t1) .GT. L/2) THEN
        y_vir = pos_y(j2,t1) - L
    ELSE
        y_vir = pos_y(j2,t1) + L
    ENDIF
    RETURN
END


REAL FUNCTION newx(old_pos,v,seed,L)
    IMPLICIT NONE
    REAL, intent(in) :: old_pos,v,L
    REAL :: theta, ran2, pi=4.0*ATAN(1.0)
    INTEGER, intent(in) :: seed
    theta = 2.0*pi*ran2(seed)
    newx = old_pos + v*cos(theta)
    IF (newx > L) newx = mod(newx,L)
    IF (newx < 0) newx = newx + L
    RETURN
END

REAL FUNCTION newy(old_pos,v,seed,L)
    IMPLICIT NONE
    REAL, intent(in) :: old_pos,v,L
    REAL :: theta, ran2, pi=4.0*ATAN(1.0)
    INTEGER, intent(in) :: seed
    theta = 2.0*pi*ran2(seed)
    newy = old_pos + v*sin(theta)
    IF (newy > L) newy = mod(newy,L)
    IF (newy < 0) newy = newy + L
    RETURN
END


REAL FUNCTION new_x_p(old_pos,v,L,p_walk,seed)
    IMPLICIT NONE
    REAL, intent(in) :: old_pos, v, L, p_walk
    REAL :: ran2, newx
    INTEGER, intent(in) :: seed
    IF (ran2(seed) .LE. p_walk) THEN
        new_x_p = newx(old_pos,v,seed,L)
    ELSE
        new_x_p = old_pos
    ENDIF
    RETURN
END

REAL FUNCTION new_y_p(old_pos,v,L,p_walk,seed)
    IMPLICIT NONE
    REAL, intent(in) :: old_pos, v, L, p_walk
    REAL :: ran2, newy
    INTEGER, intent(in) :: seed
    IF (ran2(seed) .LE. p_walk) THEN
        new_y_p = newy(old_pos,v,seed,L)
    ELSE
        new_y_p = old_pos
    ENDIF
    RETURN
END


REAL FUNCTION ran2(seed)

    IMPLICIT NONE

    INTEGER seed, im1, im2, imm1, ia1, ia2, iq1, iq2, ir1, ir2
    INTEGER ntab, ndiv
    REAL am, eps, rnmx
    PARAMETER (im1=2147483563,im2=2147483399,am=1./im1,imm1=im1-1,ia1=40014, ia2=40692,iq1=53668,iq2=52774,ir1=12211,&
    &ir2=3791,ntab=32, ndiv=1+imm1/ntab,eps=1.2e-7,rnmx=1.-eps)
    INTEGER seed2, j, k, iv(ntab), iy
    SAVE iv, iy, seed2
    DATA seed2/123456789/, iv/ntab*0/, iy/0/

    IF (seed.le.0) THEN
        seed=MAX(-seed,1)
        seed2=seed
        DO j=ntab+8, 1, -1
            k=seed/iq1
            seed=ia1*(seed-k*iq1)-k*ir1
            IF (seed.lt.0) seed=seed+im1
            IF (j.le.ntab) iv(j)=seed
        ENDDO
        iy=iv(1)
    ENDIF
    k=seed/iq1
    seed=ia1*(seed-k*iq1)-k*ir1
    IF (seed.lt.0) seed=seed+im1
    k=seed2/iq2
    seed2=ia2*(seed2-k*iq2)-k*ir2
    IF (seed2.lt.0) seed2=seed2+im2
    j=1+iy/ndiv
    iy=iv(j)-seed2
    iv(j)=seed
    IF (iy.lt.1) iy=iy+imm1
    ran2=MIN(am*iy,rnmx)

    RETURN

END



