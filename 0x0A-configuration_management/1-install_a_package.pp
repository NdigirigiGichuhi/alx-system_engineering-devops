# Installing flask using Puppet from pip3.
package { 'flask':
  ensure   => latest,
  provider => pip3,
	}
