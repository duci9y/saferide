import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Home from './pages/Home';
import WaitingRoom from './pages/WaitingRoom';

type State = {
  rideRequest?: RideRequest;
  rideStatus?: RideStatus;
  user?: User;
};

type Action =
  | { type: 'submitRide'; details: RideRequest }
  | { type: 'rideAccepted'; status: RideStatus };

type RideRequest = {
  start: string;
  end: string;
  pax: number;
};

type RideStatus = {
  licensePlate?: string;
  pickup: Date;
  dropoff: Date;
  stopsRemaining: number;
  state: 'waiting' | 'pendingPickup' | 'onboard' | 'done';
  location: string;
  shared: boolean;
};

type User = {
  fname: string;
  fullname: string;
  phone: string;
};

type SystemStatus = {
  utilizationDescription: string;
  isUp: boolean;
  announcements: string;
};

export const DispatchContext = React.createContext<React.Dispatch<Action>>(
  _ => {}
);
export const StateContext = React.createContext<State>({});

const reducer = (state: State, action: Action): State => {
  let newState = { ...state };

  if (action.type === 'submitRide') {
    newState.rideRequest = action.details;
  }
  if (action.type === 'rideAccepted') {
    newState.rideStatus = action.status;
  }
  return newState;
};

const App: React.FC = () => {
  const [state, dispatch] = React.useReducer(reducer, {});

  return (
    <React.StrictMode>
      <DispatchContext.Provider value={dispatch}>
        <StateContext.Provider value={state}>
          <Router>
            <Switch>
              <Route path="/" exact children={<Home />} />
              <Route path="/waitingroom" children={<WaitingRoom />} />
            </Switch>
          </Router>
        </StateContext.Provider>
      </DispatchContext.Provider>
    </React.StrictMode>
  );
};

export default App;
