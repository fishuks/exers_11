
class AirConditioning:
    '''
    Models an air conditioning unit.

    Attributes:
    - status (bool): On/off switch for the air conditioner.
    - temperature (int): Set temperature of the air conditioner (in degrees Celsius).

    Properties:
    - status (bool): Getter and setter for the status attribute.
    - temperature (int): Getter and setter for the temperature attribute.

    Methods:
    - switch_on(): Turns on the air conditioner and sets the temperature to the default (18 degrees Celsius).
    - switch_off(): Turns off the air conditioner and resets the temperature to None.
    - reset(): Resets the air conditioner to its default settings if it is on.
    - get_temperature(): Returns the current temperature if the air conditioner is on; otherwise, returns None.
    - raise_temperature(): Raises the temperature of the air conditioner 
    - lower_temperature(): Lowers the temperature of the air conditioner 
    - __str__(): Returns a string representation of the air conditioner's state.
        
    '''
    def __init__(self):
        self._status = False
        self._temperature = None

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value != self._status:
            return self._status
        else:
            return self._status == value

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if value != self._temperature:
            return self._temperature
        else:
            return self._temperature == value

    def switch_on(self):
        '''
        Turns on the air conditioner and sets the temperature to the default (18 degrees Celsius).

        Parameters:
        None

        Returns:
        None
        '''
        self._status = True
        self._temperature = 18

    def switch_off(self):
        '''
        Turns off the air conditioner and resets the temperature to None.

        Parameters:
        None

        Returns:
        None
        '''
        self._status = False
        self._temperature = None

    def reset(self):
        '''
        Resets the air conditioner to its default settings if it is on.

        Parameters:
        None

        Returns:
        None

        '''
        if self._status:
            self._temperature = 18

    def get_temperature(self):
        '''
        Returns the current temperature if the air conditioner is on; otherwise, returns None.

        Parameters:
        None

        Returns:
        The current temperature (in degrees Celsius) if the air conditioner is on; otherwise, None.
        '''
        if self._status:
            return self._temperature
        else:
            return None

    def raise_temperature(self):
        '''
        Raises the temperature of the air conditioner by 1 degree if the air conditioner

        Parameters:
        None

        Returns:
        None
        '''
        if self._status:
            if self._temperature < 43:
                self._temperature += 1
            

    def lower_temperature(self):
        '''
        Lowers the temperature of the air conditioner by 1 degree if the air conditioner

        Parameters:
        None

        Returns:
        None
        '''
        if self._status:
            if self._temperature > 0:
                self._temperature -= 1
            
        
    def __str__(self):
        '''
        Returns a string representation of the air conditioner's state.

        Parameters:
        None

        Returns:
        A string representing the air conditioner's state.
        '''
        if self._status:
            return f'Кондиционер включен. Температурный режим {self._temperature} '
        else:
            return 'Кондиционер выключен'


