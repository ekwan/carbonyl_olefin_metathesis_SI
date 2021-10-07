print("hello")
import sys, os
import presto, logging, re
print("modules loaded")

name = sys.argv[1]

try:
    traj = presto.config.build(f"{name}.yaml", f"{name}.chk")
    print("loaded")
    if traj.finished:
        print("trajectory is finished so quitting immediately")
        sys.exit(0)
    logging.basicConfig(level=logging.INFO, filename=f"{name}.log", format='%(asctime)s %(name)-12s  %(message)s', datefmt='%m-%d %H:%M')
    traj.run()
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(1)
