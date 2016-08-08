Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network "forwarded_port", guest: 8888, host: 3000
  config.vm.network "forwarded_port", guest: 5000, host: 9292

  # Host only network
  # config.vm.network "private_network"

  # Enable SSH agent forwarding so getting private dependencies works
  config.ssh.forward_agent = true

  # Set locale to en_US.UTF-8
  config.vm.provision "shell", inline: $script_locale

  # Install build environment
  config.vm.provision "shell", inline: $script_install, privileged: false

  config.vm.provider :parallels do |p, o|
    o.vm.box = "parallels/ubuntu-12.04"
  end
end

$script_locale = <<SCRIPT
  echo "Setting locale to en_US.UTF-8..."
  locale-gen en_US.UTF-8
  update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
SCRIPT

$script_install = File.read("./vagrant_setup.sh")
