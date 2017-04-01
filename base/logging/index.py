import logging

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('/home/kirill/Programming/Python/Book/base/logging/spam.log')
logger.addHandler(fh)

logger.info('creating an instance of auxiliary_module.Auxiliary')

myList = [1, 2, 3, 4, 5, 6]
logger.info(myList)