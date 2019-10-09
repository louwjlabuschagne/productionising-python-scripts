import os
import argparse
import logging
from pathlib import Path
from configparser import ConfigParser

LOGGING_LEVELS = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING, 'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL,
                  'D': logging.DEBUG, 'I': logging.INFO, 'W': logging.WARNING, 'E': logging.ERROR, 'C': logging.CRITICAL}
LOGGING_FORMAT = '%(asctime)-15s %(levelname)-10s %(name)-8s %(message)s'

execution_path = Path(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    description = """
    Boilerplate Code
    
    python create_ranking_df.py -c config.ini -d D
    """

    parser = argparse.ArgumentParser(prog='Boilerplate Code', 
                                     description=description)

    parser.add_argument('-c', '--config_file', 
                        type=str,
                        help='config file with passwords for various DBs')

    parser.add_argument('-d', '--debug_level', 
                        type=str, 
                        default='WARNING',
                        help='one of DEBUG (D), INFO (I), WARNING (W), ERROR (E), CRITICAL (C) - defaults to WARNING')
    parser.add_argument('-f', '--log_file', type=str, default=__file__.split('/')[-1]+'.log',
                        help='log file to write logs to - defaults to __file__.log')

    #################################################################################
    #                                 Parse Arguments                               #
    #################################################################################

    args = parser.parse_args()
    debug_level = args.debug_level
    log_file = execution_path/args.log_file
    config_file = execution_path/args.config_file

    if debug_level not in LOGGING_LEVELS.keys():
        raise Exception('--debug_level must be one of %s not %s' %
                        (', '.join(LOGGING_LEVELS.keys()), debug_level))
    logging.basicConfig(filename=log_file, filemode='w',
                        level=LOGGING_LEVELS[debug_level], format=LOGGING_FORMAT)
    logging.debug('%s called with arguments: %s' % (
        execution_path/__file__, ', '.join([k+':'+str(v) for k, v in vars(args).items()])))

    #################################################################################
    #                                 Read Config                                   #
    #################################################################################

    if not os.path.isfile(config_file):
        logging.critical('Config file %s doens\'t exist' % config_file)
        raise Exception('Config file %s doens\'t exist' % config_file)

    config = ConfigParser()
    config.read(config_file)
    logging.debug('Config for: %s read in' % (', '.join(config.sections())))