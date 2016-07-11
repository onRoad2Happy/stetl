import os
import sys

from stetl.etl import ETL
from stetl.packet import Packet
from stetl.inputs.fileinput import ZipFileInput
from tests.stetl_test_case import StetlTestCase

class ZipFileInputTest(StetlTestCase):
    """Unit tests for ZipFileInput"""

    def setUp(self):
        super(ZipFileInputTest, self).setUp()

        # Initialize Stetl
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        cfg_dict = {'config_file': os.path.join(curr_dir, 'configs/zipfileinput.cfg')}
        self.etl = ETL(cfg_dict)
    
    def test_class(self):
        chain = StetlTestCase.get_chain(self.etl)
        section = StetlTestCase.get_section(chain)
        class_name = self.etl.configdict.get(section, 'class')
        
        assert 'inputs.fileinput.ZipFileInput' == class_name
    
    def test_instance(self):
        chain = StetlTestCase.get_chain(self.etl)
        
        assert isinstance(chain.first_comp, ZipFileInput)
    
    def test_execute(self):
        chain = StetlTestCase.get_chain(self.etl)
        chain.run()
        
        result = sys.stdout.getvalue().strip().split('\n')
        assert len(result) == 6
        
    def test_name_filter(self):
        chain = StetlTestCase.get_chain(self.etl, 1)
        chain.run()
        
        result = sys.stdout.getvalue().strip().split('\n')
        assert len(result) == 2
