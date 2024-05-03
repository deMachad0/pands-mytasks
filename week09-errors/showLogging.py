# Using logging to debug code

import logging

#DEBUG will print all
logging.basicConfig(level=logging.DEBUG)
#INFO will print info and errors above it
logging.basicConfig(level=logging.INFO)
#WARN will print out warning and above it
logging.basicConfig(level=logging.WARN) 
# You can use it to print out in another file
# DEBUG,INFO,WARN
logging.basicConfig(filename = "./mainlog.log",
                    level=logging.DEBUG)

#And using format 
logging.basicConfig(filename = "./mainlog,log",
                    level=logging.WARN,
                    format="%(name)s - %(levelname)s - %(message)s-%(asctime)s-%(lineno)d")

# prog does stuff
logging.debug("We are doing stuff")
logging.info("this is information")
logging.warning("ooohh I am not certain about it")
logging.error("not good")
logging.critical("really bad")