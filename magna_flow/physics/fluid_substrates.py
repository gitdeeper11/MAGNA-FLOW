"""
Pre-configured MHD fluid substrate profiles.
Includes 10 substrates for different MHD regimes.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class FluidSubstrate:
    """MHD fluid substrate properties."""
    name: str
    density: float  # kg/m³
    kinematic_viscosity: float  # m²/s
    magnetic_diffusivity: float  # m²/s
    electrical_conductivity: float  # S/m
    rm_range: Tuple[float, float]
    re_range: Tuple[float, float]
    primary_instability: str


class FluidSubstrateLibrary:
    """Library of pre-configured MHD fluid substrates."""
    
    SUBSTRATES: Dict[str, FluidSubstrate] = {
        'plasma_deuterium': FluidSubstrate(
            name='Deuterium Tokamak Plasma',
            density=5e-6, kinematic_viscosity=1e-6, magnetic_diffusivity=1e-4,
            electrical_conductivity=1e6, rm_range=(1e6, 1e8), re_range=(1e6, 1e10),
            primary_instability='ELM peeling-ballooning'
        ),
        'hall_xenon': FluidSubstrate(
            name='Hall Thruster Xenon Plasma',
            density=1e-5, kinematic_viscosity=1e-5, magnetic_diffusivity=1e-3,
            electrical_conductivity=1e4, rm_range=(1e2, 1e4), re_range=(1e2, 1e5),
            primary_instability='Breathing mode / BHN'
        ),
        'liquid_pbbi': FluidSubstrate(
            name='Lead-Bismuth Eutectic',
            density=10500, kinematic_viscosity=1.2e-7, magnetic_diffusivity=0.7,
            electrical_conductivity=8.4e5, rm_range=(1e2, 1e4), re_range=(1e4, 1e6),
            primary_instability='Hartmann layer turbulence'
        ),
        'planetary_iron': FluidSubstrate(
            name='Liquid Iron Outer Core',
            density=7000, kinematic_viscosity=1e-6, magnetic_diffusivity=0.5,
            electrical_conductivity=1e6, rm_range=(1e5, 1e7), re_range=(1e8, 1e10),
            primary_instability='Rotating convective MHD'
        ),
        'liquid_sodium': FluidSubstrate(
            name='Liquid Sodium Coolant',
            density=927, kinematic_viscosity=6.6e-7, magnetic_diffusivity=0.09,
            electrical_conductivity=1e7, rm_range=(1e2, 1e4), re_range=(1e5, 1e7),
            primary_instability='Magnetoconvection'
        ),
        'solar_corona': FluidSubstrate(
            name='Solar Corona Plasma',
            density=1e-12, kinematic_viscosity=1e-8, magnetic_diffusivity=1e-6,
            electrical_conductivity=1e8, rm_range=(1e8, 1e12), re_range=(1e6, 1e10),
            primary_instability='Coronal mass ejection'
        ),
    }
    
    @classmethod
    def get(cls, name: str) -> FluidSubstrate:
        """Get substrate by name."""
        if name not in cls.SUBSTRATES:
            raise ValueError(f"Substrate '{name}' not found. Available: {list(cls.SUBSTRATES.keys())}")
        return cls.SUBSTRATES[name]
    
    @classmethod
    def list_all(cls) -> List[str]:
        """List all available substrates."""
        return list(cls.SUBSTRATES.keys())
    
    @classmethod
    def get_rm_range(cls, name: str) -> Tuple[float, float]:
        """Get magnetic Reynolds number range for substrate."""
        return cls.get(name).rm_range
