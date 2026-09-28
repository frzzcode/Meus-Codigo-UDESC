#include <iostream>

using namespace std;

const int LIMITE = 10;

void inserirSemRepetir(int codigos[], int& pos, int codigo) {
    for (int i = 0; i < pos; i++) {
        if (codigos[i] == codigo) {
            cout << "Codigo repetido. Nao foi inserido.\n";
            return;
        }
    }

    codigos[pos] = codigo;
    pos++;
    cout << "Codigo inserido com sucesso.\n";
}

int main() {
    int codigos[LIMITE];
    int pos = 0;
    int codigo;

    cout << "Cadastro de codigos de equipamentos (maximo de 10).\n";
    cout << "Digite um numero negativo para encerrar.\n";

    while (pos < LIMITE) {
        cout << "\nInforme o codigo: ";
        cin >> codigo;

        if (codigo < 0) {
            break;
        }

        inserirSemRepetir(codigos, pos, codigo);
    }

    cout << "\nCodigos armazenados:\n";
    for (int i = 0; i < pos; i++) {
        cout << codigos[i] << '\n';
    }

    return 0;
}