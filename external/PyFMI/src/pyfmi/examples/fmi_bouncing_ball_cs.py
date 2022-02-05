#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Modelon AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import os as O

import pylab as P
import numpy as N

from pyfmi import load_fmu

curr_dir = O.path.dirname(O.path.abspath(__file__));
path_to_fmus = O.path.join(curr_dir, 'files', 'FMUs', 'CS1.0')
path_to_fmus2 = O.path.join(curr_dir, 'files', 'FMUs', 'CS2.0')

def run_demo(with_plots=True, version='2.0'):
    """
    Demonstrates how to use PyFMI for simulation of 
    Co-Simulation FMUs (version 1.0 or 2.0).
    """
    
    if version == '1.0':
        fmu_name = O.path.join(path_to_fmus,'bouncingBall.fmu')
    else:
        fmu_name = O.path.join(path_to_fmus2,'bouncingBall.fmu')
    model = load_fmu(fmu_name)
    
    res = model.simulate(final_time=2.)
    
    # Retrieve the result for the variables
    h_res = res['h']
    v_res = res['v']
    t     = res['time']

    assert N.abs(res.final('h') - (0.0424044)) < 1e-2
    
    # Plot the solution
    if with_plots:
        # Plot the height
        fig = P.figure()
        P.clf()
        P.subplot(2,1,1)
        P.plot(t, h_res)
        P.ylabel('Height (m)')
        P.xlabel('Time (s)')
        # Plot the velocity
        P.subplot(2,1,2)
        P.plot(t, v_res)
        P.ylabel('Velocity (m/s)')
        P.xlabel('Time (s)')
        P.suptitle('FMI Bouncing Ball')
        P.show()

    
if __name__ == "__main__":
    run_demo()
