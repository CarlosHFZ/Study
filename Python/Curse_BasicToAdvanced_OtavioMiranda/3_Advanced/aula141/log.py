# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError(
            'Implemente o método log'
        )
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class LogFileMixim(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixim(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__': 
    print('\n\n')
    
    lp = LogPrintMixim()
    lp.log_error('Qualuqer coisa')
    lp.log_success('Que legal')

    lf = LogFileMixim()
    lf.log_error('Qualuqer coisa')
    lf.log_success('Que legal')

    print('\n\n')