# Biblioteca WMI

Imprime informações sobre o sua maquina,diante das solicitações 
como no no exemplo de seu funcionamento em _main.py_

###How do I install it?
<mark> pip install wmi </mark><br>

###How do I use it?
Have a look at the tutorial or the cookbook. As a quick taster, try this, to find all Automatic services which are not running and offer the option to restart each one:

**import wmi**

c = wmi.WMI()<br>
for s in c.Win32_Service(StartMode="Auto", State="Stopped"):<br>
    if raw_input("Restart %s? " % s.Caption).upper() == "Y":<br>
        s.StartService()

site do projeto: http://timgolden.me.uk/python/wmi/index.html