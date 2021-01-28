<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/1.4.8/socket.io.min.js"></script>
<script type="text/javascript" charset="utf-8">
    const socket = io('http://localhost:5000')

    socket.on('connect', () => {
      console.log("socket connected");
    });

</script>