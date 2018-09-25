import os
import re

import PyPDF2


class DCounter(object):
    '''
    For counting the number of sources in an electronic dissertation that's
    in PDF format.
    '''
    def __init__(self, filename):
        self.filename = filename


    def num_sources(self):
        with open(self.filename, 'rb') as fileObj:
            pdfReader = PyPDF2.PdfFileReader(fileObj)
            n_sources = self.count_sources(pdfReader)
        return n_sources


    def count_sources(self, pdfReader):
        '''
        Counts the number of sources in the PDF.
        If the line ends in a four-digit number and optionally the letter a
        or b, then a source citation is assumed to be complete.
        '''
        # Default.
        n_src = 0
        return n_src


if __name__ == '__main__':
    materials_path = os.path.join(
        'C:\\', 'Users', 'Admin', 'Downloads',
        'Automate_the_Boring_Stuff_onlinematerials_v.2',
        'automate_online-materials'
    )
    pdf_path = os.path.join(materials_path, 'meetingminutes.pdf')

