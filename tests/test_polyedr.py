import unittest
from unittest.mock import patch, mock_open
from pytest import approx

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_1(self):
        file_1 = """150.0	0	0	0
8	2	8
-0.5 -0.5 0.0
0.5 -0.5 0.0
0.5 0.5 0.0
-0.5 0.5 0.0
-0.5 -0.5 1.0
0.5 -0.5 1.0
0.5 0.5 1.0
-0.5 0.5 1.0
4	1    2    3    4
4	5    6    7    8"""
        with patch('shadow.polyedr.open', mock_open(read_data=file_1)):
            polyedr = Polyedr('data/test_1.geom')
            assert polyedr.projection_area() == approx(0.0)

    def test_2(self):
        file_2 = """150.0	30.0	60.0	45.0
8	2	8
-0.5 -0.5 0.0
0.5 -0.5 0.0
0.5 0.5 0.0
-0.5 0.5 0.0
-0.5 -0.5 1.0
0.5 -0.5 1.0
0.5 0.5 1.0
-0.5 0.5 1.0
4	1    2    3    4
4	5    6    7    8"""
        with patch('shadow.polyedr.open', mock_open(read_data=file_2)):
            polyedr = Polyedr('data/test_2.geom')
            assert polyedr.projection_area() == approx(0.0)

    def test_3(self):
        file_3 = """300.0	30.0	60.0	45.0
8	2	8
-0.2 -0.2 0.0
0.2 -0.2 0.0
0.2 0.2 0.0
-0.2 0.2 0.0
-0.2 -0.2 1.0
0.2 -0.2 1.0
0.2 0.2 1.0
-0.2 0.2 1.0
4	1    2    3    4
4	5    6    7    8"""
        with patch('shadow.polyedr.open', mock_open(read_data=file_3)):
            polyedr = Polyedr('data/test_3.geom')
            assert polyedr.projection_area() == approx(0.0)

    def test_4(self):
        file_4 = """40.0	60.0	0.0	0.0
8	6	24
-2.0	-2.0	2.0
-2.0	2.0	2.0
2.0	2.0	2.0
2.0	-2.0	2.0
-2.0	-2.0	-2.0
-2.0	2.0	-2.0
2.0	2.0	-2.0
2.0	-2.0	-2.0
4	1 2 3 4
4	5 6 2 1
4	3 2 6 7
4	3 7 8 4
4	1 4 8 5
4	8 7 6 5 """
        with patch('shadow.polyedr.open', mock_open(read_data=file_4)):
            polyedr = Polyedr('data/test_4.geom')
            assert polyedr.projection_area() == approx(32.0)

    def test_5(self):
        file_5 = """40.0	0.0	60.0	0.0
4	1	4
-2.0	-2.0	2.0
-2.0	2.0	2.0
2.0	2.0	2.0
2.0	-2.0	2.0
4	1    2    3    4 """
        with patch('shadow.polyedr.open', mock_open(read_data=file_5)):
            polyedr = Polyedr('data/test_5.geom')
            assert polyedr.projection_area() == approx(8.0)
