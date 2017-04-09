import unittest

class TestStringMethods(unittest.TestCase):

    def test_format(self):
        self.assertEqual('one - two', '%s - %s' % ('one', 'two')) #old
        self.assertEqual('one - two', '{} - {}'.format('one', 'two'))

    def test_old_format(self):
        n = 42
        f = 7.24
        s = 'string string'
        self.assertEqual('42 - 7.240000 - string string', '%d - %f - %s' % (n, f, s))
        self.assertEqual('        42 -   7.240000 - string string', '%10d - %10f - %10s' % (n, f, s))
        self.assertEqual('42         - 7.240000   - string string', '%-10d - %-10f - %-10s' % (n, f, s))
        self.assertEqual('0042       - 7.2400     - stri      ', '%-10.4d - %-10.4f - %-10.4s' % (n, f, s))
        self.assertEqual('0042 - 7.2400 - stri', '%.4d - %.4f - %.4s' % (n, f, s))

    def test_new_format(self):
        n = 42
        f = 7.24
        s = 'string string'
        self.assertEqual('42 - 7.24 - string string', '{} - {} - {}'.format(n, f, s))
        self.assertEqual('string string - 7.24 - 42', '{2} - {1} - {0}'.format(n, f, s))
        self.assertEqual('7.24 - string string - 42', '{f} - {s} - {n}'.format(n=42, f=7.24, s='string string'))

        d = {'n': 42, 'f': 7.24, 's': 'string'}
        self.assertEqual('7.24 - string - 42:other', '{0[f]} - {0[s]} - {0[n]}:{1}'.format(d, 'other'))

        self.assertEqual('42 - 7.240000 - string string', '{0:d} - {1:f} - {2:s}'.format(n, f, s))
        self.assertEqual('7.240000 - string string - 42', '{f:f} - {s:s} - {n:d}'.format(n=42, f=7.24, s='string string'))

        self.assertEqual('        42 -   7.240000 - string string', '{0:10d} - {1:10f} - {2:10s}'.format(n, f, s))
        self.assertEqual('        42 -   7.240000 - string string', '{0:>10d} - {1:>10f} - {2:>10s}'.format(n, f, s))
        self.assertEqual('42         - 7.240000   - string string', '{0:<10d} - {1:<10f} - {2:<10s}'.format(n, f, s))
        self.assertEqual('    42     -  7.240000  - string string', '{0:^10d} - {1:^10f} - {2:^10s}'.format(n, f, s))
        with self.assertRaises(ValueError):
            '{0:10.4d}'.format(n, f, s)
        self.assertEqual('        42 -     7.2400 - stri      ', '{0:10d} - {1:10.4f} - {2:10.4s}'.format(n, f, s))
        self.assertEqual('!!!!!!Big Sale!!!!!!', '{0:!^20s}'.format('Big Sale'))

if __name__ == '__main__':
    unittest.main()