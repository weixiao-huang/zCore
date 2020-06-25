import glob
import subprocess

# ===============Must Config========================

TIMEOUT = 10  # seconds
ZCORE_PATH = '../zCore'
BASE = 'linux/'
OUTPUT_FILE = BASE + 'test-output.txt'
RESULT_FILE = BASE + 'test-result.txt'
CHECK_FILE = BASE + 'test-check-passed.txt'

# ==============================================

with open(RESULT_FILE, "w") as f:
    index = 0
    for path in glob.glob("../rootfs/libc-test/src/*/*.exe"):
        index += 1
        path = path[9:]
        print('testing', path, end='\t')
        try:
            subprocess.run("cargo run --release -p linux-loader " + path,
                    cwd="../",shell=True, timeout=TIMEOUT, check=True)
            f.writelines(str(index)+ " " + path[15:] + " PASS\n")
            f.flush()
            print('PASS')
        except subprocess.CalledProcessError:
            f.writelines(str(index)+ " " + path[15:] + " FAILED\n")
            f.flush()
            print('FAILED')
        except subprocess.TimeoutExpired:
            f.writelines(str(index)+ " " + path[15:] + " TIMEOUT\n")
            f.flush()
            print('TIMEOUT')
