@echo off

@title : Django - Local Server Launcher


@mode con:cols=90 lines=30

for /f "delims=" %%x in (port.ini) do set port=%%x

@echo.
@echo Local server starting on port : %port% ...
@echo Edit "port.ini" to change the default local server port for this project
@echo.

start msedge.exe "http://127.0.0.1:%port%/" -inprivate
call Scripts\activate.bat && python run flask 127.0.0.1:%port%


