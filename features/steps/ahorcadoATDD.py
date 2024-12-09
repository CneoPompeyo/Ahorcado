from behave import given, when, then
from environment import esperarElemento, palabraInicial, adivinaPalabra


@given("la palabra es {palabraTest}")
def step_impl(context, palabraTest):
    dr = context.driver
    palabraInicial(dr, palabraTest)


@when("jugador ingresa {palabraTest}")
def step_impl(context, palabraTest):
    dr = context.driver
    adivinaPalabra(dr, palabraTest)

    print(f"El jugador ingresó la palabra: {palabraTest}")


@when("jugador intenta las letras {listaLetras}")
def step_impl(context, listaLetras):
    dr = context.driver
    lista = listaLetras.split(",")

    input = esperarElemento(dr, "letra")
    startBoton = esperarElemento(dr, "adivina-letra")

    for l in lista:
        input.click()
        input.send_keys(l)
        startBoton.click()


@then('se muestra {elemento} "{valor}"')
def step_impl(context, elemento, valor):
    dr = context.driver
    Msg = esperarElemento(dr, elemento)
    assert Msg.text is not valor


@then('vuelve a pantalla "{elemento}"')
def step_impl(context, elemento):
    dr = context.driver
    Msg = esperarElemento(dr, elemento)
    assert Msg.text is not None


@given('se muestra {elemento} "{valor}"')
def step_impl(context, elemento, valor):
    dr = context.driver
    Msg = esperarElemento(dr, elemento)

    assert Msg.text is not valor


@when("jugador clickea en {boton}")
def step_impl(context, boton):
    dr = context.driver
    boton = esperarElemento(dr, boton)
    boton.click()
