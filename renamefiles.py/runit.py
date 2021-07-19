#!/usr/bin/python

import os as OS
import shutil as SH
import argparse as apar


class rename:

    __name__ = 'rename' 

    def __init__ (self, name: str):
        self.name  = name
        self.files = self.obtain_files()
        
    def operate( self ):

        if( len(self.files) == 0):
            self.info(1)
            return
       
        copy = ''
        extension = ''
        prefix = 0
        path = ''
        cppath = ''

        try:

            for i in range( len(self.files) ):
                      
                # This doesn't always work, see docs
                path = self.files[i].path
                extension = OS.path.splitext(path)[-1]

        
                cppath ='./runit_dataR/{sname}__{sprefix}{sextension}'.format(spath = path,
                                                                            sname = self.name,
                                                                            sprefix = prefix,
                                                                            sextension = extension)

                # shutils ompromises metadata
                SH.copy2(path, cppath)

                prefix +=1

            self.info(3)

        except:

            self.info(2)


    def obtain_files( self ):

        data = []

        try:

           data = [f for f in OS.scandir("./runit_data/") if f.is_file()]

        except:

            self.info(0)

        return data
        


    def info(self, code: int):

        errors = {

                0: "E0: runit_data folder not found",

                1: "E1: There are not files to be renamed",

                2: "E2: Error copying data, check that the runit_dataR exists and file storage permissions",

                3: "I3: 500 OK"

                }

        print(errors[code])



parser = apar.ArgumentParser(description='Rename files', usage='%(prog)s [-n/--name] <new_name>', 
                             epilog='WTFPL license, for you <3')

parser.add_argument('-n', '--name', metavar='<new_name>', type=str, nargs=1,
                    help='new filename for files', required=True)


args = parser.parse_args( )


runit = rename(args.name[0])
runit.operate()
