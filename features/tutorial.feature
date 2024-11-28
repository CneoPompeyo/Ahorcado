Feature: showing off behave

  Scenario: Ganar el juego intentanto palabra entera
    Given la palabra es PALABRA
    When jugador ingresa PALABRA
    Then se muestra pantalla ganaste