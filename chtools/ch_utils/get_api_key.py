def get_api_key() -> str:

    import getpass
    import logging
    from companies_house.ch_utils import setup_logging

    logger = setup_logging()

    """Securely prompt for Companies House API key."""
    try:
        return getpass.getpass("Please enter your Companies House API key: ")
    except Exception as e:
        logger.error(f"Error getting API key: {e}")
        raise

if __name__ == "__main__":
    api_live_key = get_api_key()