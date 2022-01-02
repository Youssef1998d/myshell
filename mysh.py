import shell, sys

if len(sys.argv) > 1:
    sh = shell.CMD(shell.Mode.with_file, sys.argv[1])
else:
    sh = shell.CMD()


sh.run()
