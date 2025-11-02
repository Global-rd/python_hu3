import logging

# handler         hova írodjon a log üzenet (konzolra, vagy file-be)
# formatter       milyen formátumban jelenjen meg a log üzenet
# a formattertadjuk hozzá a handler-hez és a handlert adjuk a loggerhez.

file_handler = logging.FileHandler("app.log")   # file-be menjen a log
stream_handler = logging.StreamHandler()        # terminal-ba menjen a log

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')   # idő - szint - üzenet

file_handler.setFormatter(formatter)         # a formattertadjuk hozzá a handler-hez
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.ERROR)    # a file-be csak a nagyon fontos üzeneteket írjul be.
stream_handler.setLevel(logging.DEBUG)   # a terminálra mindent ki akarunk írni

logger = logging.getLogger()   # létrhozzuk a loggert. Ha nincs megadva a zárójelben név, a modul neve lesz.
logger.addHandler(file_handler)      # a loggerhez hozzáadjuk a handlert.
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")




