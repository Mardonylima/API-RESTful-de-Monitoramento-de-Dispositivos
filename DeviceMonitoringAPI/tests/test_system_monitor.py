import unittest

from DeviceMonitoringAPI.services.system_monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_system_info,
    ip_address,
    collect_system_data
)


class TestSystemMonitor(unittest.TestCase):

    def test_get_cpu_usage(self):
        cpu_usage = get_cpu_usage()
        self.assertIsInstance(cpu_usage, float)
        self.assertGreaterEqual(cpu_usage, 0)
        self.assertLessEqual(cpu_usage, 100)

    def test_get_memory_usage(self):
        memory = get_memory_usage()
        self.assertIsInstance(memory, dict)
        self.assertIn('total_mb', memory)
        self.assertIn('used_mb', memory)
        self.assertIn('free_mb', memory)
        self.assertIn('percent_used', memory)

    def test_get_disk_usage(self):
        disk = get_disk_usage()
        self.assertIsInstance(disk, dict)
        self.assertIn('Total_MB', disk)
        self.assertIn('Usado_MB', disk)
        self.assertIn('Livre_MB', disk)
        self.assertIn('Percentual_usado', disk)

    def test_ip_address(self):
        ip = ip_address()
        self.assertIsInstance(ip, str)
        self.assertGreater(len(ip), 0)

    def test_get_system_info(self):
        info = get_system_info()
        self.assertIsInstance(info, dict)
        self.assertIn('System', info)
        self.assertIn('IP_address', info)

    def test_collect_system_data(self):
        data = collect_system_data()
        self.assertIsInstance(data, dict)
        self.assertIn('cpu', data)
        self.assertIn('memory', data)
        self.assertIn('disk', data)
        self.assertIn('system_info', data)


if __name__ == '__main__':
    unittest.main()
