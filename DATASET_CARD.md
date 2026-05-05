# DisasterAgentBench Dataset Card

## Dataset

DisasterAgentBench is a benchmark for retrieval-grounded disaster assessment with drone-in-the-loop reinspection.

## Release Contents

- split manifest
- task schema
- gold-removed hidden-test task file
- frozen evaluation configuration
- benchmark freeze package
- validation materials
- released run outputs
- reproducibility scripts

## Release Boundary

The public repository does not redistribute the underlying disaster imagery bundle, private tile servers, or other non-redistributable source assets. Public task records retain event and map-source identifiers, but not the original private hosting endpoints.

## Known Limitations

- The benchmark inherits collection bias across hazard types, regions, and annotation styles.
- The UAV environment is a constrained operational simulator rather than a full physical simulator.
- Some held-out or validation summaries are diagnostic artifacts, not benchmark gold.

## Intended Use

This release is intended for benchmark evaluation, reproducibility, and diagnostic analysis of agent workflows.

## License

See `LICENSE` for the mixed-asset license notice.
