U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)


def apply_u(state):
    """Apply a quantum operation.

    Args:
        state (array[complex]): A normalized quantum state vector.

    Returns:
        array[complex]: The output state after applying U.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    return np.array(
        [
            state[0] * U[0, 0] + state[1] * U[0, 1],
            state[0] * U[1, 0] + state[1] * U[1, 1],
        ]
    )
    # APPLY U TO THE INPUT STATE AND RETURN THE NEW STATE
    pass
