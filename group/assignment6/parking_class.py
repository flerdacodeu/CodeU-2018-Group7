class Parking:
    """
    Args:
        constraints: {parking_lot: (permitted cars)}
    """
    def __init__(self, state):
        self._state = state
        self._inverted_state = self._compute_inverted_state()

    def __len__(self):
        return len(self._state)

    def _compute_inverted_state(self):
        inverted_state = list(range(len(self._state)))
        for lot, car in enumerate(self._state):
            inverted_state[car] = lot
        return inverted_state

    def get_car(self, lot):
        return self._state[lot]

    def get_lot(self, car):
        """
        :returns: int, number of a lot in which a given car is currently placed
        """
        return self._inverted_state[car]

    def get_state(self):
        return self._state

    def find_empty_lot(self):
        """
        :returns: int, number of a currently empty lot
        """
        return self._inverted_state[0]

    def move_to_empty_lot(self, car):
        """
        Moves a car from the lot to an empty lot.

        :param car: int, number of a car that is moving to an empty lot
        """
        move_from = self.get_lot(car)
        move_to = self.find_empty_lot()
        self._state[move_from] = 0
        self._state[move_to] = car
        self._inverted_state[0] = move_from
        self._inverted_state[car] = move_to
        return (move_from, move_to)
