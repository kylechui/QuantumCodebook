dev = qml.device("default.qubit", wires=2)


@qml.qnode(dev)
def convert_to_rz_rx():
    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT IN THE PICTURE USING ONLY RZ AND RX
    qml.RZ(np.pi / 2, wires=0)
    qml.RX(np.pi / 2, wires=0)
    qml.RZ(np.pi * 7 / 4, wires=0)
    qml.RX(np.pi, wires=1)

    return qml.state()
