# 🤖 EduNAO

## 🧠 Overview
Python applications for the NAO robot, designed to interact with children in nurseries and provide an easy-to-use interface for educators.  
Includes simple GUI tools and ready-to-run interaction scripts built during my robotics master studies at EPFL, part of my job at the Educalis school as Software Engineer.

<p align="center">
  <a href="./assets/nao.jpeg" title="Nao">
    <img src="./assets/nao.jpeg" width="45%" alt="Nao"/>
  </a>
</p>


## ⚙️ Technical Details

| Category | Details |
|-----------|----------|
| **Languages** | Python |
| **Frameworks / Libraries** | `naoqi`, `qi`, `PyQt5`, `SpeechRecognition`, `OpenCV` |
| **Techniques** | Human–Robot Interaction (HRI), voice and gesture recognition, basic GUI design for educators |
| **Hardware** | NAO V5 humanoid robot |
| **Environment** | Ubuntu 22.04, Python 3.10, VS Code |
| **Features** | Interactive games and dialogue scenarios for children; simple Python-based graphical interface allowing nursery educators to trigger or adapt NAO behaviors without programming knowledge |


## 📄 Media

**Tech Xplore** — [Read here](https://techxplore.com/news/2024-05-swiss-nursery-robot.html)  



## 📂 Project Structure

| Folder | Description |
|--------|--------------|
| **`Nao_executables/`** | Executable package ready for deployment on the local computer connected to the robot. |
| **`Nao_automatisation/`** | Python scripts to automatically generate NAO behaviors from a simple `.doc` thematic description. |
| **`Nao_tasks/`** | Core set of robot tasks (walking, speaking, changing volume, retrieving weather info, etc.) directly accessible from the GUI. |

---

## 🧩 Requirements

Install the following dependencies before running:
```bash
pip install naoqi tkinter PyQt5 SpeechRecognition opencv-python
```


Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Gabriel29062001/NAO_software.git
cd NAO_software/Nao_executables
```

Then launch the graphical interface or specific modules using:

```bash
python executables.py
```

## Contact
For any inquiries or support, please contact gabriel.paffi@yahoo.com