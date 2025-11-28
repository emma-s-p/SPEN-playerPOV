function [T0,A1_L,A2_L] = TimeSync(audio1, audio2)
%TimeSync finds the time stamp in the longer video that the audio syncs up.

%get the audio files in a readable format
[a1, a1_Fs] = audioread(audio1);
[a2,a2_Fs] = audioread(audio2);
N1  = length(a1);
A1_L = N1/a1_Fs;
N2 = length(a2);
A2_L = N2/a2_Fs;

%Normalize both of the audiofiles to each other

min_val = min([a1;a2]);
max_val = max([a1;a2]);

r = max_val-min_val;
a1(:,1)  = (a1(:,1)-min_val)/r;
a2(:,1) = (a2(:,1)-min_val)/r;
a1(:,2)  = (a1(:,2)-min_val)/r;
a2(:,2) = (a2(:,2)-min_val)/r;

%seperate the audio files by size
long = a1;
Fs = a1_Fs;
short = a2;
N = N2;
if N1 < N2
    long = a2;
    short = a1;
    Fs = a2_Fs;
    N = N1;
end

[cL, lags_L] = xcorr(long(:,1),short(:,1));
[cR, lags_R] = xcorr(long(:,2),short(:,2));

error = max(abs(cR))*1E-6;

[na, match_i] = max(abs(cL));

lag_match = lags_L(match_i);


r = floor((1/100)*N); %testing range
%create a array to store the audio differences 
dif = zeros(r,2);
for i = lag_match-r:lag_match+r
    for cnt = 1:r
        long_i = i+cnt-1;
        dif(cnt,1) = long_i;
        dif_L = abs(long(long_i,1)-short(cnt,1));
        dif_R = abs(long(long_i,2)-short(cnt,2));
        dif(cnt,2) = dif_L+dif_R;
    end
%check if the frequency is the same
    if max(dif(:,2)) < error
        [na, t] = min(dif(:,2));
         T = dif(t,1);
         T0 = T/Fs;
        if i == 1
            T0 = 0;
        end
        break
    end
    T0 = "No audio match availible";
end
disp(T0+"s");
end
