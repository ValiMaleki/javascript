from flask import Flask

app = Flask(__name__)


@app.route('/prime_number/<int:n>')
def prime_number(n):
    """Returns True if n is a prime number, else False."""
    if n == 1:
        return ({'Number': n, 'isPrime': False})
    if n == 2:
        return ({'Number': n, 'isPrime': False})

    for i in range(2, int(n)):
        if n % i == 0:
            return ({'Number': n, 'isPrime': False})
    return ({'Number': n, 'isPrime': True})


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
