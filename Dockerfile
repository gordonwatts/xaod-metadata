FROM gitlab-registry.cern.ch/atlas/athena/analysisbase:22.2.113

COPY ./config/atlas_setup.sh /etc/profile.d/atlas_setup.sh
