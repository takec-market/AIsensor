import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "AIsensor Docker environment ready." in captured.out
