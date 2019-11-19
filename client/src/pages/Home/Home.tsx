import React from 'react';
import { useHistory } from 'react-router-dom';
import { DispatchContext } from '../../App';

const Home: React.FC = () => {
  const [start, setStart] = React.useState('');
  const [end, setEnd] = React.useState('');
  const [pax, setPax] = React.useState(1);

  const dispatch = React.useContext(DispatchContext);

  const history = useHistory();

  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(pos => {
      console.log(pos);
    });
  }

  return (
    <form
      onSubmit={e => {
        e.preventDefault();
        dispatch({ type: 'submitRide', details: { start, end, pax } });
        history.push('/waitingroom');
        setTimeout(() => {
          dispatch({
            type: 'rideAccepted',
            status: {
              pickup: new Date(),
              dropoff: new Date(),
              stopsRemaining: 4,
              state: 'pendingPickup',
              location: 'Coolidge Corner',
              shared: true
            }
          });
        }, 1000);
      }}
    >
      <label>
        From:
        <input
          type="text"
          placeholder="Building or street address"
          onChange={e => setStart(e.target.value)}
          value={start}
        />
      </label>
      <label>
        To:
        <input
          type="text"
          placeholder="Building or street address"
          onChange={e => setEnd(e.target.value)}
          value={end}
        />
      </label>

      <label>
        Passengers:
        <input
          type="number"
          placeholder="Upto 4"
          max="4"
          min="1"
          value={pax}
          onChange={e => setPax(parseInt(e.target.value))}
        />
      </label>

      <button type="submit">Submit</button>
    </form>
  );
};

export default Home;
