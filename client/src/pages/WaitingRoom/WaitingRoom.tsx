import React from 'react';
import moment from 'moment';

import { StateContext } from '../../App';

const WaitingRoom: React.FC = () => {
  const { rideRequest, rideStatus } = React.useContext(StateContext);

  if (rideStatus !== undefined) {
    const displayETA = moment()
      .add(rideStatus.eta, 'seconds')
      .fromNow();

    return <div>You will be picked up {displayETA}</div>;
  }

  return (
    <div>
      Finding a ride from {rideRequest && rideRequest.start} to{' '}
      {rideRequest && rideRequest.end}
    </div>
  );
};

export default WaitingRoom;
