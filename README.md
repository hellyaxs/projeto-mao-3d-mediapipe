# 🖐️ Projeto Mão 3D com MediaPipe e Arduino

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/downloads/release/python-3100/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-orange?logo=google)](https://google.github.io/mediapipe/)
[![Arduino](https://img.shields.io/badge/Arduino-Uno-blue?logo=arduino)](https://www.arduino.cc/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

> 🎯 Controle um braço robótico 3D utilizando gestos das mãos capturados via webcam, combinando **MediaPipe**, **OpenCV** e **Arduino** com **PyFirmata**.

---

## 📸 Demonstração

![Demonstração do Projeto](demo.gif)

*Exemplo de detecção de gestos e controle do braço robótico.*

---

## 🚀 Tecnologias Utilizadas

| Tecnologia   | Descrição                                         |
|--------------|---------------------------------------------------|
| [Python 3.10](https://www.python.org/downloads/release/python-3100/) | Linguagem principal do projeto.           |
| [OpenCV](https://opencv.org/) | Processamento de imagens em tempo real. |
| [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) | Detecção e rastreamento de mãos. |
| [PyFirmata](https://github.com/tino/pyFirmata) | Comunicação entre Python e Arduino. |
| [Arduino Uno](https://www.arduino.cc/) | Microcontrolador para controle do braço robótico. |

---

## 🛠️ Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/hellyaxs/projeto-mao-3d-mediapipe.git
cd projeto-mao-3d-mediapipe
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure o Arduino:**

- Conecte o Arduino Uno ao computador via USB.

- Carregue o firmware padrão do Firmata no Arduino utilizando o Arduino IDE:

- Abra o Arduino IDE.

- Vá em `Arquivo > Exemplos > Firmata > StandardFirmata.`

- Selecione a porta correta e carregue o sketch no Arduino.

## 🧪 Como Utilizar
1. Inicie o script principal:

```bash

python main.py
```
2. Funcionamento:

- O sistema utilizará a webcam para detectar a posição da mão.

- Os movimentos dos dedos serão interpretados para controlar os servos do braço robótico.

- Certifique-se de que o Arduino está conectado e com o firmware do Firmata carregado.

## 📁 Estrutura do Projeto
```bash
projeto-mao-3d-mediapipe/
├── main.py               # Script principal para controle do braço robótico.
├── servo_braco3d.py      # Módulo para controle dos servos via PyFirmata.
├── testar-dedos.py       # Script para testes de detecção de dedos.
├── requirements.txt      # Lista de dependências do projeto.
├── README.md             # Documentação do projeto.
└── .gitignore            # Arquivos e pastas a serem ignorados pelo Git.
```

## 🤝 Contribuições
Contribuições são bem-vindas! Se você deseja melhorar o projeto, siga os passos abaixo:

1. Fork este repositório.

2. Crie uma nova branch: git checkout -b minha-feature.

3. Faça suas alterações e commit: git commit -m 'Minha nova feature'.

4. Envie para o seu fork: git push origin minha-feature.

5. Abra um Pull Request.

