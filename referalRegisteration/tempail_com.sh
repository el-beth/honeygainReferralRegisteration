#!/bin/bash

# this alternates protonOVPN connections and 

# STARt

ovpnConfigFilesDir="/home/endu/Downloads/protonOpenVpn/nl";
pass="montag451";

files="$(ls "$ovpnConfigFilesDir"/*)"
filesRand=""

while read i; 
	do
		filesRand="$(echo -e "$filesRand\n$RANDOM $i")";
done <<< "$files"

filesRand="$(sort <<< "$filesRand")"

files="$(sed -Ee 's/^[0-9]+ //gi' <<< "$filesRand")"

echo -e "current shuffling order is$files";

while read configFile;
	do
		if [ ! -z "$configFile" ]
			then
				if ( pgrep -x openvpn )
				then
					sudo -S killall openvpn <<< "$pass";
				fi
				ip="$(curl -s ifconfig.co/ip)";
				sudo -S openvpn --config "$configFile" --auth-user-pass /home/endu/Documents/badStuff/protonVPNcred.txt &> /dev/null <<< "$pass" & 
				sleep 2;
				while [ "$(curl -s ifconfig.co/ip)" == "$ip" ]
					do
						sleep $((RANDOM%5 + 5));
				done

				for i in {1..2}
					do
						timeout 500s python3 /home/endu/Documents/badStuff/honeygain/referalRegisteration/tempail_com.py;
				done
		fi
done <<< "$files"