Set WshShell = CreateObject("Wscript.Shell")
' Executa o bat em modo oculto (0) e não espera ele fechar (False)
WshShell.Run "cmd /c iniciar_sistema.bat", 0, False