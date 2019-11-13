# Algorithms for maximizing ride sharing efficiency

## Problem

### Overview

A user opens the app. They are able to see the average wait times either for
the entire system or for their current location. This quantity is potentially
auxiliary to the core algorithm. The default origin is the current location
if available, otherwise the user is prompted to input it. Then, a destination
is picked. The number of passengers is decided, capped at the fleet maximum
at the moment. This information is submitted to the server.

The system must assign a vehicle to this ride request. The vehicle that is
assigned to fulfil this ride request should have the best anticipated
[efficiency](#what-is-efficiency). The list of rides the vehicle is fulfiling
is updated with the current ride request placed in an order that maximizes
overall fleet effciency. An updated ETA is calculated for rides in the current
vehicle route and sent to affected clients. The vehicle receives the updated
list of rides to fulfil and calculates an updated route.

### What is efficiency?

An efficient system will:

- minimize the amount of time it takes for ride request to assigned to a vehicle
- minimize wait times between ride request and ride fulfilment
- maximize fleet capacity utilization
- minimize ride duration

in that order.

### Assumptions

- Distance calculations are not naive.
