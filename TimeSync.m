function [T0] = TimeSync(audio1, audio2)
%TimeSync finds the time stamp in the longer video that the audio syncs up.
r = 1000; %testing range
error = 10E-05; %error test

%get the audio files in a readable format
[a1, a1_Fs] = audioread(audio1);
[a2,a2_Fs] = audioread(audio2);
N1  = length(a1);
N2 = length(a2);

%WIND FILTER MAY NEED TO BE ADDED HERE

%seperate the audio files by size
long = a1;
L_F = a1_Fs;
short = a2;
N = N1;
if N1 < N2
    long = a2;
    short = a1;
    L_F = a2_Fs;
    N = N2;
end

%create a array to store the audio differences 
dif = zeros(r,2);
for i = 1:N-r
    for cnt = 1:r
        long_i = i+cnt-1;
        dif(cnt,1) = long_i;
        dif_L = abs(long(long_i,1)-short(cnt,1));
        dif_R = abs(long(long_i,2)-short(cnt,2));
        dif(cnt,2) = dif_L+dif_R;
    end
%check if the frequency is the same
    if max(dif(:,2)) < error
        T0 = i/L_F;
        if i == 1
            T0 = 0;
        end
        break
    end
    T0 = "No audio match availible";
end
disp(T0);
end