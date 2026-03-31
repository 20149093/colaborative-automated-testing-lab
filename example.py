def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def subtract(a, b):
    # This is intentionally broken for the exercise!
    # It adds instead of subtracting.
    return a + b

# Step 5: You will uncomment the lines below later in the activity
# def test_subtract():
#    assert subtract(2, 3) == -1