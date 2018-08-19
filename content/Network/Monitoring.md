Title: Network Monitoring
Date: 2016-04-03 14:46:19
Tags: Network, Monitoring



# Monitoring

network usage:

    bytes_sent(out)
    bytes_recv(in)

packets:

    packets_sent(out)
    packets_recv(in)

error_in/out:

    SELECT non_negative_derivative(mean("err_in"), 1s) AS "recv", non_negative_derivative(mean("err_out"), 1s) AS "send"
    FROM "net"
    WHERE "interface" =~ /^(vlan|eth|ens|bond).*/ AND $timeFilter
    GROUP BY time($__interval), "host", "interface" fill(none)

drop_in/out:

    SELECT non_negative_derivative(mean("drop_in"), 1s) AS "recv", non_negative_derivative(mean("drop_out"), 1s) AS "send"
    FROM "net"
    WHERE "interface" =~ /^(vlan|eth|ens|bond).*/ AND $timeFilter
    GROUP BY time($__interval), "host", "interface" fill(none)

