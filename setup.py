import cx_Freeze
executables = [cx_Freeze.Executable(
    script="jogo.py", icon="imagens/chuva-hamburguer.ico")]

cx_Freeze.setup(
    name="Chovendo-Hambúrguer",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["imagens",]
                           }},
    executables=executables
)