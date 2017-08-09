from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(File):
    present = [
        "/etc/keepalived/keepalived.conf"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "keepalived"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled
            assert s.is_running


def test_packages(Package):
    present = [
        "keepalived"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed
