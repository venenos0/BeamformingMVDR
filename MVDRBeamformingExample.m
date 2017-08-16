 %% MVDR Beamforming
% Apply an MVDR beamformer to a 5-element ULA. The incident angle of the
% signal is 45 degrees in azimuth and 0 degree in elevation. The signal
% frequency is 1/100 hertz. The carrier frequency is 300 MHz.

% Copyright 2015 The MathWorks, Inc.

t = [0:.1:200]';
fr = .01;
xm = sin(2*pi*fr*t);
c = physconst('LightSpeed');
fc = 300e6;
rng('default');
incidentAngle = [45;0];
sULA = phased.ULA('NumElements',5,'ElementSpacing',0.5);
x = collectPlaneWave(sULA,xm,incidentAngle,fc,c);
noise = 0.1*(randn(size(x)) + 1j*randn(size(x)));
rx = x + noise;

%%
% Compute the beamforming weights
sMVDR = phased.MVDRBeamformer('SensorArray',sULA,...
    'PropagationSpeed',c,'OperatingFrequency',fc,...
    'Direction',incidentAngle,'WeightsOutputPort',true);
[y,w] = step(sMVDR,rx);

%w = s


%%
% Plot the signals
plot(t,real(rx(:,3)),'r:',t,real(y))
xlabel('Time')
ylabel('Amplitude')
legend('Original','Beamformed');
%%
% Plot the array response pattern using the MVDR weights
pattern(sULA,fc,[-180:180],0,'PropagationSpeed',c,...
    'Weights',w,'CoordinateSystem','rectangular',...
    'Type','powerdb');

save -mat MVDR rx y  %% MVDR Beamforming
% Apply an MVDR beamformer to a 5-element ULA. The incident angle of the
% signal is 45 degrees in azimuth and 0 degree in elevation. The signal
% frequency is 1/100 hertz. The carrier frequency is 300 MHz.

% Copyright 2015 The MathWorks, Inc.

t = [0:.1:200]';
fr = .01;
xm = sin(2*pi*fr*t);
c = physconst('LightSpeed');
fc = 300e6;
rng('default');
incidentAngle = [45;0];
sULA = phased.ULA('NumElements',5,'ElementSpacing',0.5);
x = collectPlaneWave(sULA,xm,incidentAngle,fc,c);
noise = 0.1*(randn(size(x)) + 1j*randn(size(x)));
rx = x + noise;

%%
% Compute the beamforming weights
sMVDR = phased.MVDRBeamformer('SensorArray',sULA,...
    'PropagationSpeed',c,'OperatingFrequency',fc,...
    'Direction',incidentAngle,'WeightsOutputPort',true);
[y,w] = step(sMVDR,rx);

%w = s


%%
% Plot the signals
plot(t,real(rx(:,3)),'r:',t,real(y))
xlabel('Time')
ylabel('Amplitude')
legend('Original','Beamformed');
%%
% Plot the array response pattern using the MVDR weights
pattern(sULA,fc,[-180:180],0,'PropagationSpeed',c,...
    'Weights',w,'CoordinateSystem','rectangular',...
    'Type','powerdb');

save MATLABdata.mat rx y w c fc t incidentAngle







