Feature: Ahorcado
  Scenario: Repetir letra usada
    Given la palabra es PALABRA
    When jugador intenta las letras B,M,B
    Then se muestra mensaje "usada"

  Scenario: Ganar el juego intentando palabra entera
    Given la palabra es PALABRA
    When jugador ingresa PALABRA
    Then se muestra mensaje "ganaste"
    
    Scenario: Reiniciar juego luego de ganar
      Given se muestra mensaje "ganaste"
      When jugador clickea en reiniciar
      Then se muestra mensaje "empezar_juego"

  Scenario: Perder el juego intentando palabra entera
    Given la palabra es PALABRA
    When jugador ingresa MANZANA
    Then se muestra mensaje "perdiste"

  Scenario: Reiniciar juego luego de perder
    Given se muestra mensaje "perdiste"
    When jugador clickea en reiniciar
    Then se muestra mensaje "empezar_juego"

  Scenario: Quedarse sin vidas
    Given la palabra es PALABRA
    When jugador intenta las letras E,O,U,I,A,C,M,G
    Then se muestra mensaje "perdiste"

  Scenario: Ganar completando letras
    Given la palabra es PALABRA
    When jugador intenta las letras A,T,P,L,U,R,B
    Then se muestra mensaje "ganaste"
    