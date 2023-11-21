/*

* Carlos Luilquer Almeida Santos
* matrícula: 20150465
* Método da Falsa POsição
* Função: f(x) = x^3 -x -1

*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale.h> //necessário para usar setlocale

//função
float f(float x)
{
    float y;
    y = pow(x, 3) - x - 1;

    return y;
}

//método da falsa posição

float metodo(float a, float b, float toleracia)
{
    //variaveis
    float fa, fb, x_ns, fx_ns;

    //calculo da função no ponto a
    fa = f(a);

    //calculo da função no ponto b
    fb = f(b);

    //calculo de x_ns
    x_ns = (b * f(a) - f(b) * a) / (f(a) - f(b));

    //calculo da função no ponto x_ns
    fx_ns = f(x_ns);

    //laço de repetição, enquanto o módulo da função é maior que a tolerancia erro
    while (fabs(f(x_ns)) > toleracia)
    {
        //calculo de x_ns
        x_ns = (b * f(a) - f(b) * a) / (f(a) - f(b));
        //calculo da função no ponto x_ns
        fx_ns = f(x_ns);

        //verifica se o multiplicação da fa e fx_ns é menor que zero

        if (fa * fx_ns < 0)
        {
            //b recebe o valor de x_ns
            b = x_ns;
            //fb recebe o valor de f_xns
            fb = fx_ns;
        }
        else
        {
            //a recebe o valor de x_ns
            a = x_ns;
            //fa recebe o valor de fx_ns
            fa = fx_ns;
        }
    }

    //retorna o valor de x
    return x_ns;
}

int main()
{
    //variaveis
    float a, b, toleracia, x_ns;

    setlocale(LC_ALL, "Portuguese"); // para visualizar portugues corretamente

    printf("Método da falsa posição \n");
    printf("\n função f(x) = x^3 -x -1 \n");

    printf("\n Digite limite inferior (ponto A): ");
    scanf("%f", &a);

    printf("\n Digite limite superior (ponto B): ");
    scanf("%f", &b);

    printf("\n Digite a tolerância (erro): ");
    scanf("%f", &toleracia);

    x_ns = metodo(a, b, toleracia);

    printf("Raiz aproximada = %0.4f \n", x_ns);

    system("pause");

    return 0;
}
