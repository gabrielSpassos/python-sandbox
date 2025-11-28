from click.testing import CliRunner
from hello.main import hello

def test_hello_command():
    runner = CliRunner()
    
    result = runner.invoke(hello, ["Gabriel"])
    
    assert result.exit_code == 0
    assert "Hello, Gabriel!" in result.output
