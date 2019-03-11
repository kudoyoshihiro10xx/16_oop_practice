class Version:
    """バージョンを表現したクラス
    ex:
        Python 3.7.0
        Ruby 2.5.8
        MacOS(HighSierra) 10.13.6
    """

    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def info(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def major_version_up(self):
        self.major += 1

    def minor_version_up(self):
        self.minor += 1

    def patch_version_up(self):
        self.patch += 1


if __name__ == "__main__":
    # 実際のPythonのバージョンを表現
    python_version = Version(3, 7, 0)

    print(python_version.info())

    # MacOS(High Sierra)10.13.6 を表現
    high_sierra_version = Version(10, 13, 6)

    print(high_sierra_version.info())
